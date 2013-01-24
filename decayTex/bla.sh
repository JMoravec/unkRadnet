#!/bin/bash
latex decay.tex &&
latex decay.tex &&
dvipdf decay.dvi &&
evince decay.pdf
