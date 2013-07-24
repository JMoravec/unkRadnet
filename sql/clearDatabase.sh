#!/bin/bash
rm radnet.db
sqlite3 radnet.db < intial.sql
sqlite3 radnet.db
