from solution import tar_to_zip


def main():
    tar_to_zip('one.tar', 'two.tar.gz', 'three.tar.bz2')

    tar_to_zip('one.tar', 'two.tar.gz', 'three.tar.bz2', zippath='./out')


if __name__ == '__main__':
    main()
