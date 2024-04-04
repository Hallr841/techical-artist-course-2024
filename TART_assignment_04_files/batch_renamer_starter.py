import os
import logging
import argparse
import shutil


def initialize_logger(print_to_screen=False):
    """
    Creates a logger

    Args:
        print_to_screen: for printing to screen as well as file
    """
    app_title = 'BatchRenamer'
    version_number = '1.0.0'
    source_path = os.path.dirname(os.path.realpath(__file__))
    logfile_name = f'{app_title}.log'
    logfile = os.path.join(source_path, logfile_name)

    print(f'Logfile is {logfile}')

    logger = logging.getLogger(f'{app_title} Logger')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter(f'%(asctime)s - %(name)s {version_number} - '
                                  '%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(file_handler)

    if print_to_screen:
        console = logging.StreamHandler()
        logger.addHandler(console)
        console.setFormatter(formatter)

    return logger


def parse_arguments():
    """
    Parses arguments provided via command line with argparse

    """
    parser = argparse.ArgumentParser(
        prog='BatchRenamer',
        description='Renames files in specified folder')
    
    parser.add_argument('-fp', '--filepath',
                        required=True,
                        help='filepath to look at')
    parser.add_argument('-nf', '--new_folder',
                        default=None,
                        help='new folder to move or copy files to')
    parser.add_argument('-cp', '--copy_files',
                        action="store_true",
                        help='set to copy files instead of renaming them')
    parser.add_argument('-ow', '--overwrite',
                        action="store_true",
                        help='allow overwriting files')
    parser.add_argument('-ft', '--filetypes',
                        nargs='+',
                        default=None,
                        help='filetypes to modify')
    parser.add_argument('-find', '--strings_to_find',
                        nargs='+',
                        default=None,
                        help='strings to find in filename for replacement')
    parser.add_argument('-rep', '--string_to_replace',
                        default='',
                        help='string to replace strings_to_find with')
    parser.add_argument('-pre', '--prefix',
                        default='',
                        help='prefix to add to modified filenames')
    parser.add_argument('-suf', '--suffix',
                        default='',
                        help='suffix to add to modified filenames')
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='sets the logger to print to screen')

    args = parser.parse_args()
    return args


def modify_file(logger, existing_name, new_name, copy_mode=True, force=False):
    """
    Renames or copies a file if it exists
    Only overwrites files if force is True

    Args:
        existing_name: full filepath of a file that should already exist
        new_name: full filepath for the new name
        copy_mode: copy instead of rename
        force: allows overwriting files
    """
    if os.path.isfile(existing_name):
        if not os.path.isfile(new_name) or force:
            if copy_mode:
                shutil.copy(existing_name, new_name)
            else:
                shutil.move(existing_name, new_name)
        else:
            logger.error(f"File '{new_name}' already exists.")
    else:
        logger.error(f"File '{existing_name}' does not exist.")


class BatchRenamer:
    def __init__(self, verbose=False):
        self.logger = initialize_logger(verbose)

    def process_folder(self, filepath, new_folder, copy_files, overwrite, filetypes,
                       strings_to_find, string_to_replace, prefix, suffix):
        # This method could use or wrap the existing 'process_folder_with_params' function's logic
        pass

def process_folder(logger, filepath, new_folder, copy_files, overwrite, filetypes,
                   strings_to_find, string_to_replace, prefix, suffix):
    if not os.path.isdir(filepath):
        logger.error(f"Invalid folder path: '{filepath}'")
        return
    
def process_folder_with_params(filepath, new_folder, copy_files, overwrite, filetypes,
                               strings_to_find, string_to_replace, prefix, suffix, verbose=False):
    logger = initialize_logger(verbose)
    process_folder(
        logger,
        filepath,
        new_folder,
        copy_files,
        overwrite,
        filetypes,
        strings_to_find,
        string_to_replace,
        prefix,
        suffix
    )

    if new_folder and not os.path.exists(new_folder):
        os.makedirs(new_folder)

    for filename in os.listdir(filepath):
        file_path = os.path.join(filepath, filename)
        if os.path.isfile(file_path):
            if not filetypes or os.path.splitext(filename)[1][1:] in filetypes:
                new_filename = filename
                if strings_to_find:
                    strings_to_find.sort(key=len, reverse=True)
                    for string_to_find in strings_to_find:
                        new_filename = new_filename.replace(string_to_find, string_to_replace)

                if filename.endswith(".ma"):
                    new_filename = prefix + new_filename

                if filename.endswith(".txt"):
                    new_filename = "NOTE_" + new_filename[:filename.rfind(".")] + "_TEMP" + filename[filename.rfind("."):]
                elif filename.endswith(".png"):
                    new_filename = "T_" + os.path.splitext(new_filename)[0] + ".png"

                new_file_path = os.path.join(new_folder, new_filename) if new_folder else os.path.join(filepath, new_filename)
                modify_file(logger, file_path, new_file_path, copy_mode=copy_files, force=overwrite)


def main(renamer_args):
    logger = initialize_logger(renamer_args.get('verbose', False))  # Set default value to False if 'verbose' key not found
    logger.info('Logger Initiated')

    process_folder(
        logger,
        filepath=renamer_args['filepath'],
        new_folder=renamer_args['new_folder'],
        copy_files=renamer_args['copy_files'],
        overwrite=renamer_args['overwrite'],
        filetypes=renamer_args['filetypes'],
        strings_to_find=renamer_args['strings_to_find'],
        string_to_replace=renamer_args['string_to_replace'],
        prefix=renamer_args['prefix'],
        suffix=renamer_args['suffix']
    )



if __name__ == '__main__':
    arguments = parse_arguments()
    renamer_args_dict = {
        'filepath': arguments.filepath,
        'new_folder': arguments.new_folder,
        'copy_files': arguments.copy_files,
        'overwrite': arguments.overwrite,
        'filetypes': arguments.filetypes,
        'strings_to_find': arguments.strings_to_find,
        'string_to_replace': arguments.string_to_replace,
        'prefix': arguments.prefix,
        'suffix': arguments.suffix
    }
    main(renamer_args_dict)
