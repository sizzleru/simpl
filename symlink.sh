#!/bin/sh

FIND='/usr/bin/find'
PATTERN='.*v[0-9]+\_[0-9]+\_[0-9]+\.py$'
FOLDER_ROOT=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ ! $(command -v "${FIND}") ]; then
	echo "command find (${FIND}) was not found!"
	exit 1
fi

for folder in $(
	"${FIND}" * \
		-type 'f' \
		-regex "${PATTERN}" \
		-print0 | xargs -0 dirname -- | sort -u
); do
	file=$("${FIND}" "${folder}" -type 'f' -regex "${PATTERN}" -printf '%f\0' | sort -rz | head -zn 1 | sed 's/\x0//g')

	cd "${FOLDER_ROOT}/${folder}"
	ln -vfs "${file}" 'latest.py'
	cd "${FOLDER_ROOT}"
done
