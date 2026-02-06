# Python Language — DECORATORS

## Part 2: Decorators in Real Frameworks (Django & FastAPI Style)

> **Goal of this part**
>
> Till now, decorators were **your code wrapping your code**.
>
> Now you will see:
> - How **frameworks use decorators to control execution flow**
> - How decorators sit between **request → logic → response**
> - Why decorators are called **framework glue** 🧩
>
> After this part, decorators will stop feeling like a Python trick and start feeling like a **system design tool**.

---

## 1️⃣ Big Picture — What Framework Decorators ACTUALLY Do

In real frameworks, decorators usually do one (or more) of these:

- Authentication / Authorization 🔐
- Routing (URL → function) 🌐
- Validation 🧪
- Logging & Metrics 📊
- Dependency Injection 🧩

Important mindset shift:

> **Framework decorators do NOT add features**
>
> They **control WHEN and IF your function runs**.

---

## 2️⃣ Django Example — `@login_required`

### What you write:

```python
@login_required
def dashboard(request):
    return "Welcome to dashboard"
```

### What Django REALLY does internally (simplified):

```python
def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")
        return view_func(request, *args, **kwargs)
    return wrapper
```

At definition time:
```
dashboard = login_required(dashboard)
```

---

### Execution Flow (VERY IMPORTANT)

```
HTTP Request
   ↓
Decorator wrapper
   ↓
Authentication check
   ↓
Original view function
   ↓
HTTP Response
```

Your function is **never the first code executed**.

---

## 3️⃣ Mental Model — Decorator as a SECURITY GATE 🚧

Think of it like an office:

- User arrives at gate
- Security guard checks ID
- Only then office access

Decorator = security guard
Function = office

---

## 4️⃣ FastAPI Example — `@app.get("/users")`

### What you write:

```python
@app.get("/users")
def get_users():
    return ["Alice", "Bob"]
```

### What you THINK happens ❌
> FastAPI just calls `get_users()`

### What ACTUALLY happens ✅

- `@app.get()` **registers** your function
- It stores:
  - URL path
  - HTTP method
  - Function reference

Your function is **NOT executed immediately**.

---

## 5️⃣ FastAPI Decorator — Simplified Internals

```python
class App:
    def get(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
```

Usage:
```python
@app.get("/users")
def get_users():
    pass
```

Execution meaning:

```
app.get("/users") → decorator
@decorator → stores function
```

---

## 6️⃣ Request-Time vs Definition-Time (FRAMEWORK CRITICAL)

### Definition Time:

- Decorators run
- Routes are registered
- Permissions are attached

### Request Time:

- Wrapper executes
- Validation happens
- Business logic runs

This separation is **core to frameworks**.

---

## 7️⃣ Multiple Decorators in Frameworks 🔗

Example:

```python
@login_required
@permission_required("admin")
def admin_panel(request):
    pass
```

Equivalent to:

```python
admin_panel = login_required(
    permission_required("admin")(admin_panel)
)
```

### Execution Order:

- Bottom decorator runs FIRST
- Top decorator runs LAST

Flow:
```
Request
 → permission check
 → login check
 → view
```

---

## 8️⃣ Decorators for Validation 🧪

Example idea:

```python
def validate_json(func):
    def wrapper(request):
        if not request.json:
            return "Invalid JSON"
        return func(request)
    return wrapper
```

Used heavily in APIs.

---

## 9️⃣ Why Frameworks LOVE Decorators ❤️

Because decorators:

- Keep business logic clean
- Separate concerns
- Enable configuration via syntax
- Avoid inheritance hell

Decorator = composition over inheritance

---

## 🔟 Gold Questions 🎯

### Q1. Why do frameworks use decorators heavily?

Because decorators allow cross-cutting concerns (auth, logging, validation) without touching core logic.

---

### Q2. Does `@app.get()` execute the function?

No. It **registers** the function and stores metadata.

---

### Q3. Difference between request-time and definition-time?

- Definition-time → decorators run
- Request-time → wrapper logic runs

---

### Q4. Are framework decorators function-based or class-based?

Both. Many frameworks use **class-based decorators internally**.

---

## 🧠 FINAL MENTAL MODEL (LOCK THIS)

```
Decorator = control layer
Framework = orchestrator
Function = pure business logic
```

Your function is a **plug-in**, not the boss.

---


✨ END — Decorators Part 2

