import os
import datetime

if os.path.exists("reports") == False:
    os.mkdir("reports")
    
now_date = datetime.datetime.now()
file_name = f"{now_date.strftime("%Y-%m-%d_%H-%M-%S")}.txt"
report_path = os.path.join("reports", file_name)

report_content = f"Relatório feito em {now_date.strftime("%d/%m/%Y %H:%M:%S")}"

with open(report_path, 'w') as file:
    file.write(report_content)
    
print("Relatório gerado com sucesso!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
