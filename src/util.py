"""Utility functions."""

from owlready2 import locstr


def en(s):
    """Return `s` as an English location string."""
    return locstr(s, lang="en")


def enGB(s):
    """Return `s` as an British-English location string."""
    return locstr(s, lang="en-GB")


def enUS(s):
    """Return `s` as an American-English location string."""
    return locstr(s, lang="en-US")


def pl(s):
    """Return `s` as a plain literal string."""
    return locstr(s, lang="")


def add_altLabel(entry, label):
    """Append a new altLabel to an EMMO entry.

    If the entry already has an altLabel list, append the value;
    otherwise create altLabel as a new list containing the value.
    """
    if hasattr(entry, "altLabel"):
        entry.altLabel.append(label)
    else:
        entry.altLabel = [label]
