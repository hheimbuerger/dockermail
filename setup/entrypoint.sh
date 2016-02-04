#!/bin/sh

export CONFIGFILE="/mail_settings/config.json"

if [ ! -f "${CONFIGFILE}" ]; then
	setup "${CONFIGFILE}"
fi

exec "${@}"
