#!/usr/bin/env bash
set -euo pipefail

PKG="org.safesep.probe"
PERM="android.permission.CAMERA"
ROOT="$(cd "$(dirname "$0")" && pwd)"
OUT="$ROOT/out"
mkdir -p "$OUT"

AAPT2="$(find "$ANDROID_HOME/build-tools" -type f -name aapt2 | sort -V | tail -1)"
APKSIGNER="$(find "$ANDROID_HOME/build-tools" -type f -name apksigner | sort -V | tail -1)"
ANDROID_JAR="$ANDROID_HOME/platforms/android-35/android.jar"

test -x "$AAPT2"
test -x "$APKSIGNER"
test -f "$ANDROID_JAR"

"$AAPT2" link   -o "$OUT/probe-unsigned.apk"   -I "$ANDROID_JAR"   --manifest "$ROOT/AndroidManifest.xml"

keytool -genkeypair -noprompt   -keystore "$OUT/test.keystore"   -storepass safesep -keypass safesep   -alias safesep -keyalg RSA -keysize 2048 -validity 1   -dname "CN=SAFESEP Synthetic Test" >/dev/null 2>&1

"$APKSIGNER" sign   --ks "$OUT/test.keystore"   --ks-pass pass:safesep   --key-pass pass:safesep   --out "$OUT/probe.apk"   "$OUT/probe-unsigned.apk"

adb install -r "$OUT/probe.apk"
adb shell pm revoke "$PKG" "$PERM" || true

state() {
  adb shell dumpsys package "$PKG" |
    grep -F "$PERM:" |
    head -1 |
    tr -d '\r'
}

BEFORE="$(state)"
echo "before=$BEFORE"
echo "$BEFORE" | grep -q "granted=false"

adb shell pm grant "$PKG" "$PERM"
AFTER_GRANT="$(state)"
echo "after_grant=$AFTER_GRANT"
echo "$AFTER_GRANT" | grep -q "granted=true"

adb shell pm revoke "$PKG" "$PERM"
AFTER_REVOKE="$(state)"
echo "after_revoke=$AFTER_REVOKE"
echo "$AFTER_REVOKE" | grep -q "granted=false"

adb uninstall "$PKG"

cat > "$OUT/permission-sanity.txt" <<EOF
package=$PKG
permission=$PERM
initial=denied
after_grant=granted
after_revoke=denied
interpretation=platform permission-state sanity check only; not a vulnerability claim
EOF

cat "$OUT/permission-sanity.txt"
