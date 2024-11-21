from datetime import datetime, timezone
import win32serviceutil
import servicemanager
import win32service
import win32event
import traceback
# import main
import os

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'WebBackend'
    _svc_display_name_ = 'Web Backend Developer'
    _svc_description_ = 'Windows App service Python.'

    def __init__(self, args):
        try:
            win32serviceutil.ServiceFramework.__init__(self, args)
            self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
            self.is_alive = True
            self.log(f'{datetime.now(timezone.utc)} - WebBackend service successfully started.')
        except Exception as e:
            error_message = f'{datetime.now(timezone.utc)} - Service failed to start: {str(e)}\n{traceback.format_exc()}'
            servicemanager.LogErrorMsg(error_message)
            self.log(error_message)

    def SvcStop(self):
        try:
            self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
            win32event.SetEvent(self.hWaitStop)
            self.is_alive = False
            self.log(f'{datetime.now(timezone.utc)} - WebBackend service is stopping.')
        except Exception as e:
            error_message = f'{datetime.now(timezone.utc)} - Error while stopping the service: {str(e)}\n{traceback.format_exc()}'
            servicemanager.LogErrorMsg(error_message)
            self.log(error_message)
            
    def SvcDoRun(self):  
        self.log(f'{datetime.now(timezone.utc)} - WebBackend service started.')
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                            servicemanager.PYS_SERVICE_STARTED,
                            (self._svc_name_, ''))
        try:
            self.main()
        except Exception as e:
            error_message = f'{datetime.now(timezone.utc)} - Error occurred: {str(e)}\n{traceback.format_exc()}'
            self.log(error_message)
            servicemanager.LogErrorMsg(error_message)
            self.SvcStop()

    def main(self):
        self.log(f'{datetime.now(timezone.utc)} - Main function started.')
        try:
            main.main()  # Ana main
            self.log(f'{datetime.now(timezone.utc)} - WebBackend transaction completed successfully.')
        except Exception as e:
            error_message = f'{datetime.now(timezone.utc)} - Error occurred in main function: {str(e)}\n{traceback.format_exc()}'
            self.log(error_message)
            servicemanager.LogErrorMsg(error_message)
            self.SvcStop()

    def log(self, message):
        try:
            with open("", "a", encoding='utf-8') as log_file:
                log_file.write(f"{message}\n")
        except Exception as e:
            error_message = f'{datetime.now(timezone.utc)} - Error writing to log file: {str(e)}\n{traceback.format_exc()}'
            print(error_message)
            servicemanager.LogErrorMsg(error_message)

if __name__ == '__main__':
    if len(os.sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        try:
            win32serviceutil.HandleCommandLine(MyService)
        except Exception as e:
            print(f'{datetime.now(timezone.utc)} - Error: {str(e)}\n{traceback.format_exc()}')