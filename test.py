import os
import zipfile

class UnpakingProject:
    def __init__(self, build_path ="C:/Users/ademnichenko/Desktop/anim_compress/IOS", unpack_path = "C:/Program Files/Epic Games/UE_4.15/Engine/Binaries/Win64"):
        self.build_path = build_path
        self.unpak_path = unpack_path
        self.ipa_folder_name = "extractedIPA"
        self.pak_folder_name = "unpakedPAK"

    def ResearchFile(self, path, extension):
        result = False
        file = ""
        directory = ""
        for dir, subdirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(extension):
                    result = True
                    file = filename
                    directory = dir
        return file, directory, result

    def UnzipIPA(self):
        search = self.ResearchFile(self.build_path, ".ipa")
        if True in search:
            zip_file = zipfile.ZipFile("{0}/{1}".format(search[1], search[0]), 'r')
            zip_file.extractall("{0}/{1}".format(search[1], self.ipa_folder_name))
            zip_file.close()
            #     return True
            # else:
            #     return False

    def UnpakPAK(self):
        search = self.ResearchFile("{0}".format(self.build_path), ".pak")
        if True in search:
            with open("{0}/unpak.bat".format(self.build_path), 'w') as batch:
                batch.write("cd {0}/\nUnrealPak.exe {1}/{2} -Extract {3}/{4}".format(self.unpak_path, search[1], search[0], self.build_path, self.pak_folder_name))
            os.system("{0}/unpak.bat".format(self.build_path))
            #     return True
            # else:
            #     return False

    def GetPackagesSize(self):
        total_size = 0
        size_statistic = ""
        for dirpath, dirnames, filenames in os.walk("{0}".format(self.build_path)):
            if dirpath.find("Packages") != -1:
                for dirname in os.listdir(dirpath):
                    for drp, drn, fn in os.walk("{0}/{1}".format(dirpath, dirname)):
                        for f in fn:
                            fp = os.path.join(drp, f)
                            total_size += os.path.getsize(fp)
                    size_statistic += size_statistic.join("{0} = {1}Mb\n".format(dirname, total_size / 1000000))
                    total_size = 0
                    break
            else:
                for f in filenames:
                    if f.endswith(".ipa"):
                        fp = os.path.join(dirpath, f)
                        ipa_size = os.path.getsize(fp)
                        size_statistic += size_statistic.join("IPA Size - {0}Mb\n".format(ipa_size / 1000000))
        return size_statistic
