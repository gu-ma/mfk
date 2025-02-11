set APPPATH=C:\Program Files\Derivative\TouchDesigner.2023.12120\bin
set TDPATH=C:\Users\Guillaume\Documents\Clouds\OneDrive - iart ag\MfK\TD\Main
start "%APPPATH%" "%APPPATH%\TouchDesigner.exe" -gpuformonitor 1 "%TDPATH%\Main_Lite_New.toe"
start "%APPPATH%" "%APPPATH%\TouchDesigner.exe" -gpuformonitor 0 "%TDPATH%\Streamdiffusion.toe"