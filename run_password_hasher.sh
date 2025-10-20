#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_password_hasher..."
wine "run_password_hasher" || ./"run_password_hasher" "$@"
