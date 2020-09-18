from paste.request import parse_formvars

class ObjectPublisher(object):

    def __init__(self, root):
        self.root = root

    def __call__(self, environ, start_response):
        fields = parse_formvars(environ)
        obj = self.find_object(self.root, environ)
        response_body = obj(**fields.mixed())
        start_response('200 OK', [('content-type', 'text/html')])
        return [str.encode(response_body)]

    def find_object(self, obj, environ):
        path_info = environ.get('PATH_INFO', '')
        if not path_info or path_info == '/':
            return obj
        path_info = path_info.lstrip('/')
        parts = path_info.split('/', 1)
        next = parts[0]
        if len(parts) == 1:
            rest = ''
        else:
            rest = '/' + parts[1]
        
        assert not next.startswith('_')
       
        next_obj = getattr(obj, next)
       
        environ['SCRIPT_NAME'] += '/' + next
        environ['PATH_INFO'] = rest
       
        return self.find_object(next_obj, environ)

class Root(object):

    # The "index" method:
    def __call__(self):
        return '''
        <!DOCTYPE html>
        <html style="background-color:mediumseagreen;">
       
         <header style="background: url(https://bradaronson.com/wp-content/uploads/2012/04/Performance-Measures.jpg); background-size: cover;">
            <br>
            <h1 style="color:RoyalBlue; text-align:center; font-size:400%; "> 
            Unit Conversion </h1>
            <br>
         </header>

            <div>
             <h2 style="color:black; text-align:center;">How to convert unit!</h2>

                <p style="border-style: solid; margin-right:25%; margin-left:25%; font-size:100%; padding:10px;"> 
                    <strong>
                    1 - Insert the temperature or distance inside the box. <br>
                    2 - Select the convertion type button.<br>
                    3 - Press the submit button.<br>
                    </strong>
                </p>
            </div>

            <br>

            <body> 
         
            <!-- Fahrenheit and Celcius convertion-->
            <div1 style="position:relative; left:80px;">
               
                <h3> Fahrenheit and Celcius convertion </h3>
                <form action="fahrenheit_to_celcius" method="get" >
                Temperature: <input type="number" name="temp" step="any">  <input type="submit">  <input type="reset" value="Reset">
                <br>
             ConvertionType:
                <input type="radio" name="type" value="fahrenheit_to_celcius">
                <label for="fahrenheit_to_celcius">Fahrenheit to Celcius</label>
                <input type="radio" name="type" value="celcius_to_fahrenheit">
                <label for="celcius_to_fahrenheit">Celcius to Fahrenheit</label>
                <br><br>
             </form>
            </div1>
            
            <hr>

            <!-- Kilometer and Miles convertion-->
            <div2 style="position:relative; left:80px;">
               
                <h3> Kilometer and Miles convertion </h3>
                <form action="kilometers_to_miles" method="get">
                Distance: <input type="number" name="distance" step="any">  <input type="submit">  <input type="reset" value="Reset">
                <br>
                ConvertionType:
                    <input type="radio" name="type" value="kilometers_to_miles">
                    <label for="kilometers_to_miles">kilometers to Miles</label>
                    <input type="radio" name="type" value="miles_to_kilometers">
                    <label for="miles_to_kilometers">Miles to Kilometer</label>
                <br><br>
                </form>
            </div2>
            
            <hr>

            <!-- Meter and Feet convertion-->
            <div3 style="position:relative; left:80px;">
                <h3> Meter and Feet convertion </h3>
                <form action="meter_to_feet" method="get">
                Distance: <input type="number" name="distance" step="any"> <input type="submit">  <input type="reset" value="Reset">
                <br>
                ConvertionType:
                    <input type="radio" name="type" value="meter_to_feet">
                    <label for="meter_to_feet">Meter to Feet</label>
                    <input type="radio" name="type" value="feet_to_meter">
                    <label for="feet_to_meter">Feet to Meter</label>
                 <br><br>
                 </form>
            </div3>

            <hr>

            <!-- Inches to Centimeters-->
            <div4 style="position:relative; left:80px;">
                <h3> Inches to Centimeters </h3>
                <form action="inches_to_centimeters" method="get">
                Distance: <input type="number" name="distance" step="any">  <input type="submit">  <input type="reset" value="Reset">
                <br>
                ConvertionType:
                    <input type="radio" name="type" value="inches_to_centimeters">
                    <label for="inches_to_centimeters">Inches to Centimenters</label>
                    <input type="radio" name="type" value="centimeters_to_inches_">
                    <label for="centimeters_to_inches_">Centimenters to Inches</label>
                <br><br>
                </form>
            </div4>

            <hr>

            <footer style="color:darkblue;text-align:center;">
                <p>Created by: Mauro De Moraes<br>
                <a href="mailto:demoraes.mauro@gmail.com">demoraes.mauro@gmail.com</a></p>

            </footer>
        </html> 
        '''
      

    def fahrenheit_to_celcius(self, temp, type):
        if type == "fahrenheit_to_celcius":
            temp =(float(temp) - 32)*0.5556
        else:
            temp = (float(temp)*1.8)+32
        return '''
        <html style="background-color:mediumseagreen;">
            <button onclick="goBack()">Go Back</button>
            <script>
                function goBack() {
                 window.history.back();
                }
            </script>
            <h1 style="color:red; font-size:40px; height: 25em; display:flex; align-items:top; justify-content: center; ">  The converted temperature is %s 
            </h1>
        </html>''' % str("{:.2f}".format(temp))
    

    def kilometers_to_miles(self, distance, type):
        if type == "kilometers_to_miles":
            distance = (float(distance)*0.62137)
        else:
            distance = (float(distance)*1.609344)
        return '''
        <html style="background-color:mediumseagreen;">
            <button onclick="goBack()">Go Back</button>
             <script>
                function goBack() {
                 window.history.back();
                }
             </script>
            <h1 style="color:red; font-size:40px; height: 25em; display:flex; align-items:top; justify-content: center; "> The converted distance is %s
            </h1>
        </html>'''% str("{:.2f}".format(distance))

    def meter_to_feet(self, distance, type):
        if type == "meter_to_feet":
            distance = (float(distance)/0.3048)
        else:
            distance = (float(distance)*0.3048)
        return '''
        <html style="background-color:mediumseagreen;">
            <button onclick="goBack()">Go Back</button>
             <script>
                function goBack() {
                 window.history.back();
                }
             </script>
            <h1 style="color:red; font-size:40px; height: 25em; display:flex; align-items:top; justify-content: center; "> The converted distance is %s
            </h1>
        </html>'''% str("{:.2f}".format(distance))

    def inches_to_centimeters(self, distance, type):
        if type == "inches_to_centimeters":
            distance = (float(distance) * 2.54)
        else:
            distance = (float(distance) / 2.54)
        return '''
        <html style="background-color:mediumseagreen;">
            <button onclick="goBack()">Go Back</button>
             <script>
                function goBack() {
                 window.history.back();
                }
             </script>
            <h1 style="color:red; font-size:40px; height: 25em; display:flex; align-items:top; justify-content: center; "> The converted distance is %s
            </h1>
        </html>'''% str("{:.2f}".format(distance))   
        # return 'The distance is %s' % str(distance)

app = ObjectPublisher(Root())

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

