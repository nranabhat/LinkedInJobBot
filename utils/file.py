import time
import os

import utils.logger as logger
from utils.logger import MessageTypes


def displayWriteResults(lineToWrite: str):
    try:
        #logger.logDebugMessage(lineToWrite, MessageTypes.WARNING)
        __writeResultsIntoFile(lineToWrite)
    except Exception as e:
        logger.logDebugMessage("❌ Error in DisplayWriteResults", MessageTypes.ERROR, e) 


def __writeResultsIntoFile(text: str):
    timeStr = time.strftime("%Y%m%d")
    directory = "data"
    fileName = "Applied Jobs DATA - " + timeStr + ".txt"
    filePath = os.path.join(directory, fileName)

    try:
        os.makedirs(directory, exist_ok=True)  # Ensure the 'data' directory exists.

        # Open the file for reading and writing ('r+' opens the file for both)
        with open(filePath, 'r+', encoding="utf-8") as file:
            lines = []
            for line in file:
                if "----" not in line:
                    lines.append(line)
            file.seek(0)  # Go back to the start of the file
            file.truncate()  # Clear the file
            file.write("---- Applied Jobs Data ---- created at: " + timeStr + "\n")
            file.write("---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result " + "\n")
            for line in lines:
                file.write(line)
            file.write(text + "\n")
    except FileNotFoundError:
        with open(filePath, 'w', encoding="utf-8") as f:
            f.write("---- Applied Jobs Data ---- created at: " + timeStr + "\n")
            f.write("---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result " + "\n")
            f.write(text + "\n")
    except Exception as e:
        logger.logDebugMessage("Error in writeResults", logger.MessageTypes.ERROR, e)


# def __writeResults(text: str):
#     timeStr = time.strftime("%Y%m%d")
#     fileName = "Applied Jobs DATA - " +timeStr + ".txt"
#     try:
#         with open("data/" +fileName, encoding="utf-8" ) as file:
#             lines = []
#             for line in file:
#                 if "----" not in line:
#                     lines.append(line)
                
#         with open("data/" +fileName, 'w' ,encoding="utf-8") as f:
#             f.write("---- Applied Jobs Data ---- created at: " +timeStr+ "\n" )
#             f.write("---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result "   +"\n" )
#             for line in lines: 
#                 f.write(line)
#             f.write(text+ "\n")
            
#     except:
#         with open("data/" +fileName, 'w', encoding="utf-8") as f:
#             f.write("---- Applied Jobs Data ---- created at: " +timeStr+ "\n" )
#             f.write("---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result "   +"\n" )

#             f.write(text+ "\n")