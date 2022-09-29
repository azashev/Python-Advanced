def concatenate(*args, **kwargs):
    all_args = "".join(args)

    for key, value in kwargs.items():
        if key in all_args:
            all_args = all_args.replace(key, value)

    return all_args

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))