from django.shortcuts import HttpResponse

def page(repuist):
    html = """
    <h1>
    Yangi vazifa yaratish
    </h1>
    <label>Vazifa nomi: 
        <input type="text"/> 
    </label>
    <br>
    <br>
    <label>Tavsif: </label>
    <textarea></textarea>
    <br>
    <br>
    <label>Mudati: 
        <input type="date"/> 
    </label>
    <br>
    <br>
    <label>Muhimlik darajasi:</label>
    <select>
        <option>Past</option>
        <option>O'rta</option>
        <option>Yuqori</option>
    </select>
    <br>
    <br>
    <button>Vazifani saqlash</button>
    
    """
    return HttpResponse(html)