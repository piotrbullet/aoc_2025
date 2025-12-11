def read_inputs(path: str) -> str:
    with open(path, "r") as f:
        text = f.read()
    return text