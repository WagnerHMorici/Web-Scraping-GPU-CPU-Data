import csv


# Format data to row format
def get_data(data):
    return [data['product'], data['price'], data['information'], data['url']]



# Open File and write each row
def write_csv(data):
    
    header = ['Product', 'Price', 'Description', 'Url']
    
    
    with open('gpu.csv', 'w') as f:
        
        writer = csv.writer(f)
        
        writer.writerow(header)
        
        for i in data:
            
            data = get_data(i)
        
            writer.writerow(data)