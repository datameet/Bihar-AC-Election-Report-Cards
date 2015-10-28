
#Renaming files
rename 's/tabula-SUP.B-/Data__Supaul__Nirmali__/' *.*
rename 's/.P-/__/' *.*
rename 's/ /_/' *.*
rename 's/tabula-Quality Affected - Madhubani district/Data__Quality__Affected__Madhubani/' *.*





#Count the no of rows in a folder
find . -name '*.csv' | xargs wc -l


----------------------------
cd Bihar-AC-Election-Report-Cards
python merge.py -f ./../../data/in_processing/khagaria/Khagaria-Alauli/national_rural_drinking_water_programme -o alauli_nrdw
python merge.py -f ./../../data/in_processing/khagaria/Khagaria-Beldaur/national_rural_drinking_water_programme -o beldaur_nrdw
python merge.py -f ./../../data/in_processing/khagaria/Khagaria-Beldaur/national_rural_drinking_water_lab_testing -o beldaur_lab_results
python merge.py -f ./../../data/in_processing/khagaria/Khagaria-Beldaur/sanitation -o beldaur_sanitation_results
python merge.py -f ./../../data/in_processing/khagaria/Khagaria-Khagaria/national_rural_drinking_water_programme -o khagaria_nrdw
python merge.py -f ./../../data/in_processing/khagaria/Khagaria-Khagaria/sanitation -o khagaria_sanitation_results
python merge.py -f ./../../data/in_processing/khagaria/Khagaria-Parbatta/national_rural_drinking_water_programme -o parbatta_nrdw


python merge.py -f ./../../data/in_processing/pashchim_champaran/bagaha/national_rural_drinking_water_programme -o bagaha_nrdw
python merge.py -f ./../../data/in_processing/pashchim_champaran/bettiah/national_rural_drinking_water_programme -o bettiah_nrdw
python merge.py -f ./../../data/in_processing/pashchim_champaran/chanpatiya/national_rural_drinking_water_programme -o chanpatiya_nrdw
python merge.py -f ./../../data/in_processing/pashchim_champaran/chanpatiya/sanitation -o chanpatiya_sanitation_results
python merge.py -f ./../../data/in_processing/pashchim_champaran/lauriya/national_rural_drinking_water_programme -o lauriya_nrdw
python merge.py -f ./../../data/in_processing/pashchim_champaran/narkatiaganj/national_rural_drinking_water_programme -o narkatiaganj_nrdw
python merge.py -f ./../../data/in_processing/pashchim_champaran/nautan/national_rural_drinking_water_programme -o nautan_nrdw
python merge.py -f ./../../data/in_processing/pashchim_champaran/ramnagar/national_rural_drinking_water_programme -o ramnagar_nrdw
python merge.py -f ./../../data/in_processing/pashchim_champaran/sikta/national_rural_drinking_water_programme -o sikta_nrdw
python merge.py -f ./../../data/in_processing/pashchim_champaran/valmiki_nagar/national_rural_drinking_water_programme -o valmiki_nagar_nrdw



python merge.py -f ./../../data/in_processing/madhubani/babubarhi/national_rural_drinking_water_programme -o babubarhi_nrdw
python merge.py -f ./../../data/in_processing/madhubani/benipatti/national_rural_drinking_water_programme -o benipatti_nrdw
python merge.py -f ./../../data/in_processing/madhubani/bisfi/national_rural_drinking_water_programme -o bisfi_nrdw
python merge.py -f ./../../data/in_processing/madhubani/harlakhi/national_rural_drinking_water_programme -o harlakhi_nrdw
python merge.py -f ./../../data/in_processing/madhubani/jhanjharpur/national_rural_drinking_water_programme -o jhanjharpur_nrdw
python merge.py -f ./../../data/in_processing/madhubani/khajauli/national_rural_drinking_water_programme -o khajauli_nrdw
python merge.py -f ./../../data/in_processing/madhubani/laukaha/national_rural_drinking_water_programme -o laukaha_nrdw
python merge.py -f ./../../data/in_processing/madhubani/madhubani/national_rural_drinking_water_programme -o madhubani_nrdw
python merge.py -f ./../../data/in_processing/madhubani/phulparas/national_rural_drinking_water_programme -o phulparas_nrdw
python merge.py -f ./../../data/in_processing/madhubani/rajnagar/national_rural_drinking_water_programme -o rajnagar_nrdw

python merge.py -f ./../../data/in_processing/saharsa/mahishi/national_rural_drinking_water_programme -o mahishi_nrdw
python merge.py -f ./../../data/in_processing/saharsa/saharsa/national_rural_drinking_water_programme -o saharsa_nrdw
python merge.py -f ./../../data/in_processing/saharsa/simri_bakhtiyarpur/national_rural_drinking_water_programme -o simri_bakhtiyarpur_nrdw
python merge.py -f ./../../data/in_processing/saharsa/sonbarsa/national_rural_drinking_water_programme -o sonbarsa_nrdw


python merge.py -f ./../../data/in_processing/supaul/chattapur/national_rural_drinking_water_programme -o chattapur_nrdw
python merge.py -f ./../../data/in_processing/supaul/nirmali/national_rural_drinking_water_programme -o nirmali_nrdw


python merge.py -f ./../../data/in_processing/supaul/pipra/national_rural_drinking_water_programme -o pipra_nrdw
python merge.py -f ./../../data/in_processing/supaul/supaul/national_rural_drinking_water_programme -o supaul_nrdw
python merge.py -f ./../../data/in_processing/supaul/triveniganj/national_rural_drinking_water_programme -o triveniganj_nrdw



python merge.py -f ./../../data/in_processing/madhubani/babubarhi/sanitation -o babubarhi_sanitation
python merge.py -f ./../../data/in_processing/madhubani/benipatti/sanitation -o benipatti_sanitation
python merge.py -f ./../../data/in_processing/madhubani/bisfi/sanitation -o bisfi_sanitation
python merge.py -f ./../../data/in_processing/madhubani/harlakhi/sanitation -o harlakhi_sanitation
python merge.py -f ./../../data/in_processing/madhubani/jhanjharpur/sanitation -o jhanjharpur_sanitation
python merge.py -f ./../../data/in_processing/madhubani/khajauli/sanitation -o khajauli_sanitation
python merge.py -f ./../../data/in_processing/madhubani/laukaha/sanitation -o laukaha_sanitation
python merge.py -f ./../../data/in_processing/madhubani/madhubani/sanitation -o madhubani_sanitation
python merge.py -f ./../../data/in_processing/madhubani/phulparas/sanitation -o phulparas_sanitation
python merge.py -f ./../../data/in_processing/madhubani/rajnagar/sanitation -o rajnagar_sanitation


python merge.py -f ./../../data/in_processing/madhubani/water_quality -o madhubani_water_quality




