import os
import zipfile

class UnpakingProject:
    def __init__(self, build_path ="C:/Users/ademnichenko/Desktop/anim_compress/IOS", unpack_path = "D:/SVN/LiS_Production/Dev/UnrealEngine-4.15.1/Engine/Binaries/Win64"):
        self.build_path = build_path
        self.unpak_path = unpack_path
        self.ipa_folder_name = "extractedIPA"
        self.pak_folder_name = "unpakedPAK"
    def UnzipIPA(self):
        for dir, subdirs, files in os.walk(self.build_path):
            for filename in files:
                if filename.endswith(".ipa"):
                    zip_file = zipfile.ZipFile("{0}/{1}".format(self.build_path, filename), 'r')
                    if zip_file.extractall("{0}/{1}".format(self.build_path, self.ipa_folder_name)):
                        zip_file.close()
                        return True
                    else:
                        return False
    def UnpakPAK(self):
        for dir, subdirs, files in os.walk("{0}/{1}".format(self.build_path,self.ipa_folder_name)):
            for filename in files:
                if filename.endswith(".pak"):
                    with open("{0}/unpak.bat".format(self.build_path), 'w') as batch:
                        batch.write("{0}/UnrealPak.exe {1}/{2} -Extract {3}/{4}".format(self.unpak_path, dir, filename, self.build_path, self.pak_folder_name))
                    os.system("{0}/unpak.bat".format(self.build_path))
                    return True
    def GetPackagesSize(self):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk("{0}/{1}".format(self.build_path, self.pak_folder_name)):
            if dirpath.find("Packages") != -1:
                for dirname in os.listdir(dirpath):
                    for drp, drn, fn in os.walk("{0}/{1}".format(dirpath, dirname)):
                        for f in fn:
                            fp = os.path.join(drp, f)
                            total_size += os.path.getsize(fp)
                    print("{0} = {1}Mb".format(dirname, total_size / 1000000))
                    total_size = 0
                break

unpak = UnpakingProject()
unpak.UnzipIPA()
unpak.UnpakPAK()
unpak.GetPackagesSize()