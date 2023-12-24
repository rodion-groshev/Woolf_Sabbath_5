def parse_input(user_input):
    """Parser helper. Splits commands and args, lowercasse command."""

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
