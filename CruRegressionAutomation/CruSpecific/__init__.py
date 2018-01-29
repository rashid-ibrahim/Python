#############################################################################
# Author: Rashid "Lee" Ibrahim                                              #
# Original Date: 4/28/2017                                                  #
# Most Recent Update: 4/28/2017                                             #
# Purpose: Control script for cru testing methods/functions                 #
#############################################################################

import pyautogui as gui
gui.PAUSE = 1.0
gui.FAILSAFE = True
#from ..CruTestOps import GeneralFunctions as gen

def clientMaintenanceTests():
    import CruSpecific.clientMaintenanceTestsScript
    testResult = clientMaintenanceTestsScript.main()
    return testResult

def orderMaintenanceTests():
    import CruSpecific.orderMaintenanceTestsScript
    testResult = orderMaintenanceTestsScript.main()
    return testResult

def followUpTests():
    import CruSpecific.followUpTestScript
    testResult = followUpTestScript.main()
    return testResult

def setupMaintenanceTests():
    import CruSpecific.setupMaintenanceTestsScript
    testResult = setupMaintenanceTestsScript.main()
    return testResult

def printMaintenanceTests():
    import CruSpecific.printMaintenanceTestsScript
    testResult = printMaintenanceTestsScript.main()
    return testResult

def checkingAccountTests():
    import CruSpecific.checkingAccountTestsScript
    testResult = checkingAccountTestsScript.main()
    return testResult

def reprintRequestTests():
    import CruSpecific.reprintRequestTestsScript
    testResult = reprintRequestTestsScript.main()
    return testResult

def usaaImportTests():
    import CruSpecific.usaaImportTestsScript
    testResult = usaaImportTestsScript.main()
    return testResult

def productionMonitorTests():
    import CruSpecific.productionMonitorTestsScript
    testResult = productionMonitorTestsScript.main()
    return testResult

def batchStatusTests():
    import CruSpecific.batchStatusTestsScript
    testResult = batchStatusTestsScript.main()
    return testResult

def companyMaintenanceTests():
    import CruSpecific.companyMaintenanceTestsScript
    testResult = companyMaintenanceTestsScript.main()
    return testResult

def vinMaintenanceTests():
    import CruSpecific.vinMaintenanceTestsScript
    testResult = vinMaintenanceTestsScript.main()
    return testResult

def asqProcessingTests():
    import CruSpecific.asqProcessingTestsScript
    testResult = asqProcessingTestsScript.main()
    return testResult

def asqAlgorithmMaintenanceTests():
    import CruSpecific.asqAlgorithmMaintenanceTestsScript
    testResult = asqAlgorithmMaintenanceTestsScript.main()
    return testResult

def agencyMaintenanceTests():
    import CruSpecific.agencyMaintenanceTestsScript
    testResult = agencyMaintenanceTestsScript.main()
    return testResult

def orderProcessingTests():
    import CruSpecific.orderProcessingTestsScript
    testResult = orderProcessingTestsScript.main()
    return testResult

def documentProcessingTests():
    import CruSpecific.documentProcessingTestsScript
    testResult = documentProcessingTestsScript.main()
    return testResult

def deliveryMaintenanceTests():
    import CruSpecific.deliveryMaintenanceTestsScript
    testResult = deliveryMaintenanceTestsScript.main()
    return testResult

def orderLookupTests():
    import CruSpecific.orderLookupTestsScript
    testResult = orderLookupTestsScript.main()
    return testResult

def scanningTests():
    import CruSpecific.scanningTestsScript
    testResult = scanningTestsScript.main()
    return testResult

def printEnvelopesTests():
    import CruSpecific.printEnvelopesTestsScript
    testResult = printEnvelopesTestsScript.main()
    return testResult

def startTests():
    resultsArr = []
    
    resultsArr.append(clientMaintenanceTests())
    resultsArr.append(orderMaintenanceTests())
    resultsArr.append(followUpTests())
    resultsArr.append(setupMaintenanceTests())
    resultsArr.append(printMaintenanceTests())
    resultsArr.append(checkingAccountTests())
    resultsArr.append(reprintRequestTests())
    resultsArr.append(usaaImportTests())
    resultsArr.append(productionMonitorTests())
    resultsArr.append(batchStatusTests())
    resultsArr.append(companyMaintenanceTests())
    resultsArr.append(vinMaintenanceTests())
    resultsArr.append(asqProcessingTests())
    resultsArr.append(asqAlgorithmMaintenanceTests())
    resultsArr.append(agencyMaintenanceTests())
    resultsArr.append(orderProcessingTests())
    resultsArr.append(documentProcessingTests())
    resultsArr.append(deliveryMaintenanceTests())
    resultsArr.append(orderLookupTests())
    resultsArr.append(scanningTests())
    resultsArr.append(printEnvelopesTests())
    
    return resultsArr

#Stops script from being run directly.
if __name__ == '__main__':
    print("This script can NOT be run directly")
    input()
    exit()
