
##ex1
##
##member_with_error = ['sam_liao@payez.com.tw',
## 'kevin_chen@payez.com.tw',
##‘I_LOVE_SAM',
## 'jc_wang@payez.com.tw', '456']
##
## ['sam_liao@payeasy.com.tw', 'kevin_huang@payeasy.com.tw',
## 'jc_wang@payeasy.com.tw']
##
##1. create list variable member_without_error to store data
##2. for loop member_with_error to iterate string
##3. use if else to find out which string should be processed
##4. replace string to correct one
##5. append correct string to member_without_error

member_with_error = ['sam_liao@payez.com.tw', 'kevin_chen@payez.com.tw', 'I_LOVE_SAM', 'jc_wang@payez.com.tw', '456']
print ('original data:')
print (member_with_error)

member_without_error = []

for i in member_with_error:
    if '@' in i:
        member_without_error.append(i)

print ('filtered data:')
print (member_without_error)


##ex2
## staffs = [['sam', 613, 'sam_liao@payez.com.tw'],
##                    ['charlotte', 712, 'charlotte_wang@payeasy.com.tw'], 
##                    ['kevin', 617, 'kevin_huang@康迅.公司.台灣']]
## ['payez.com.tw', 'payeasy.com.tw', '康迅.公司.台灣']


staffs = [['sam', 613, 'sam_liao@payez.com.tw'],
['charlotte', 712, 'charlotte_wang@payeasy.com.tw'], 
['kevin', 617, 'kevin_huang@康迅.公司.台灣']]
print ('original data:')
print (staffs)
staffs_domain = []
for i in staffs:
    staffs_domain.append(i[2].split('@')[1])
print ('extract domain:')
print (staffs_domain)



