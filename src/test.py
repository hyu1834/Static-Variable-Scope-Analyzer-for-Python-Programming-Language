## @file main.py
# @author Hiu Hong Yu (AHMCT)
# @package main
# This is the main script for standalone TASAS

import os
import sys

import io_utils
import tasasAPI

# ## @brief process each specified report to extract contents
# #@details
# #Function will directly export report contents as JSON file the same directory where the pdf is located.
# # @param digital_tasas - digital tasas instance
# # @param non_digital_tasas - non digital tasas instance
# # @param report_pdf_path - path to the pdf that is being process
# # @return None
# def process_report(digital_tasas, non_digital_tasas, report_pdf_path):
# 	# get the base directory, filename, and file extension
# 	basename, extension = dirent_utils.get_file_basename_extension(report_pdf_path)
# 	basedir = dirent_utils.get_directory_basename(report_pdf_path)
# 	report_contents = {}

# 	# first determine rather this PDF is in digital format or not
# 	digital = pdf_utils.is_digital_pdf(report_pdf_path)
# 	if not digital:
# 		io_utils.stdlog("Is not Digital")
# 		report_contents = non_digital_tasas.tasas_report_reader(basedir, basename, report_pdf_path)
# 	else:
# 		# start the process of extracting report contents by digital report
# 		# extract the data from the boundary box
# 		report_contents = digital_tasas.tasas_report_reader(basedir, basename, report_pdf_path)
# 		report_contents["NARR"] = tasas_narr_utils.tasas_narr_analyzer(report_contents["NARRATIVE"])

# 	# output result into json file
# 	json_encoder.json_dumper("%s.json"%os.path.join(basedir,basename), report_contents)


## @brief A standalone report contents extraction program using TASASAPI
# @return None
def main():
	report_pdf_path = None
	report_xml_path = None

	# parse through arguements for setting
	index = 0
	argc = len(sys.argv)
	while(index < argc):
		if "-h" == argv or "--help" == argv:
			help()
			return
		elif "-px" == argv or "--pdfxml" == argv:
			index += 1
			if index < argc:
				report_pdf_path, report_xml_path = sys.argv[index].split(":")
			else:
				io_utils.stderr("Dangling -px or --pdfxml flag on command line", terminate = True)
		elif "-xp" == argv or "--xmlpdf" == argv:
			index += 1
			if index < argc:
				report_xml_path, report_pdf_path = sys.argv[index].split(":")
			else:
				io_utils.stderr("Dangling -xp or --xmlpdf flag on command line", terminate = True)
		elif "-p" == argv or "--pdf" == argv:
			index += 1
			if index < argc:
				report_pdf_path = sys.argv[index]
			else:
				io_utils.stderr("Dangling -p or --pdf flag on command line", terminate = True)
		elif "-x" == argv or "--xml" == argv:
			index += 1
			if index < argc:
				report_xml_path = sys.argv[index]
			else:
				io_utils.stderr("Dangling -x or --xml flag on command line", terminate = True)
		else:
			io_utils.stderr("Unrecognized command line option: %s"%sys.argv[index], terminate = True)

		index += 1

	# create TASASAPI instance
	tasas_api = tasasAPI.TASASAPI()
	# process the report
	tasas_api.process_report(report_xml_path, report_pdf_path, export_json = True, ignore_warning = True)
	

if __name__ == "__main__":
	main()