# To create a Carbon Emission Calculator to measure Gas combustion in a Industry
gas_amount=float(input("Enter gas amount(kg): "))
gas_type=input("Enter Gas Type: ""(ng or lpg?):")
combustion_efficiency=float(input("Enter Combustion Efficiency: ")) #fraction value
emission_factor= "Constant value for each Gas Type"
ng="Natural Gas"
lpg="LPG Gas"
if gas_type=="ng":
    emission_factor= 3.08 #unit of emission_factors are in Kg CO2/Kg of Gas
elif gas_type=="lpg" :
    emission_factor= 2.90 # emission factor is a constant value for each Gas
else:
    print("Gas Type is not available")
    exit()

CO2_emission= gas_amount*emission_factor*combustion_efficiency
print("CO2_emission(kg):",CO2_emission)




