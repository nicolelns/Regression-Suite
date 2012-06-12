import json 

def image_page_maker(img_data):
    	    
    	n = 0
    	  
    	page = open('/Users/nsmith/Regression-Suite/TESTS/cut/desktop/qa/data/image_rendition_test.html', 'w')
    	
    	page.write("<html><body>")
    	
    	for each in img_data:
    	
    	    src = img_data[n]
    	    alt = "FOO"
    	    
    	    if src != "jcr:primaryType" or src != "original" or src != "createdBy":
    		
    	        page.write("<img src='" + src + "' alt='" + alt + "'/>")
    	        n += 1
    	    
    	page.write("</body></html>")
    	
    	page.close()
    	
def data_organizer():
	
    f = open('/Users/nsmith/Regression-Suite/TESTS/cut/desktop/qa/data/json/imagetool.json').read()
    data = json.loads(f)
    	
    foo = data.values()
    bar = foo[2].values()
    images = bar[3].keys()
    
    bar2 = bar[2]
    #height = bar2[?]
    #width = bar2.[?]
    print bar2
    image_page_maker(images)
    	
data_organizer()
