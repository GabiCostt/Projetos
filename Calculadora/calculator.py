from calculator_factories import *

def main():
    root = make_root()
    make_label(root)
    make_display(root)
    root.mainloop()


if __name__ == '__main__':
    main()
