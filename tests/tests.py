from ArgumentParser import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.addArgument('--arg', int, default=10, choices=[10, 15, 20])
    options = parser.parseArguments()
    print(dir(options))