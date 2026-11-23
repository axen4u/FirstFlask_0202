from flask import Flask, render_template, request

app = Flask(__name__)



# Slide 6: A working web app fits in five lines

@app.route("/")
def hello():
    return "Hello, World!"



# Slide 7: Routes map URLs to Python functions

@app.route("/home")
def home():
    return "Home page"


@app.route("/about")
def about():
    return "About us"


@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"


@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"



# Slide 8: Quick check & Challenge

@app.route("/welcome")
def index():
    return "Welcome!"


@app.route("/hi/<name>")
def hi(name):
    return f"Hi, {name}!"


@app.route("/double/<int:n>")
def double(n):
    return f"{n * 2}"


# Challenge: Write a route where /age/20 shows "You are 20"
@app.route("/age/<int:age>")
def show_age(age):
    return f"You are {age}"



# Slide 9: GET reads data, POST sends it

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            name = "Please enter a name"
        # Menghubungkan ke template greet.html (Slide 13)
        return render_template("greet.html", name=name)
    return """
    <h2>Greeting App</h2>
    <form method="post">
      <label>What's your name?</label><br>
      <input name="name" placeholder="Enter name">
      <button type="submit">Send</button>
    </form>
    """



# Slide 10: Templates keep HTML out of your Python code

@app.route("/hello/<name>")
def template_hello(name):
    return render_template("hello.html", name=name)



# Slide 13: Exercise (Square)

@app.route("/square/<int:n>")
def square(n):
    return f"Square of {n} is {n ** 2}"


# ==========================================
# Tugas: Parsing Parameter menggunakan Method POST
# ==========================================
@app.route("/tugas", methods=["GET", "POST"])
@app.route("/form", methods=["GET", "POST"])
def tugas_post():
    hasil = None
    if request.method == "POST":
        # Parsing parameter yang dikirim melalui method POST
        nama = request.form.get("nama")
        pesan = request.form.get("pesan")
        hasil = {
            "nama": nama,
            "pesan": pesan
        }
    return render_template("index.html", hasil=hasil)


if __name__ == "__main__":
    app.run(debug=True)
