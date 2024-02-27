from zeep import Client
#https://www.dataaccess.com/webservicessererver/NumberConvertion.wso?WSDL
client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result = client.service.NumberToWords(5)
print(result)

result = client.service.NumberToDollars(2)
print(result)