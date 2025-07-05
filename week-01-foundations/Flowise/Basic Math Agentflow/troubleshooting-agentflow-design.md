# Flowise Agent: Calculator Tool Troubleshooting Notes

## Goal

Build an agent that answers math questions like:
```
What is 2 + 2?
```
...by calling a calculator tool rather than solving natively.

---

## 🔧 Initial Setup

### Agent Node
- **Model:** `gpt-3.5-turbo`
- **Prompt:**
  ```
  You are a calculator. Use the calculator tool for math problems and respond only with the result.
  ```

### Tool Node
- **Tool Type:** Calculator
- **Input Argument Name:** `input`
- **Input Argument Value:** `{{input}}`

### Issue
The agent responded:
```
I don't know how to do that.
```

---

## ✅ Attempt to Fix Notes

1. **The agent must be explicitly allowed to call tools.**
2. **The tool must be defined as a function with a valid schema.**

## 1. Agent Configuration

### Prompt:
```text
Use the calculator function to evaluate math expressions. Only respond with the result.
```

### Parameters > BaseOptions:
```json
{
  "tool_choice": "auto"
}
```

> Note: Add this in the `BaseOptions` field in the Agent node UI (expand the `{}` section).

---

### 2. Replace Calculator with Function Tool

Instead of the calculator tool, use Flowise's **Function Tool** to define a proper schema:

- **Tool Name:** `calculator`
- **Description:** `Evaluate a math expression and return the result`
- **Parameters:**
  - `input` → `string` → `The math expression to evaluate`

This automatically provides OpenAI with the valid JSON function spec:
```json
{
  "name": "calculator",
  "description": "Evaluate a math expression and return the result.",
  "parameters": {
    "type": "object",
    "properties": {
      "input": {
        "type": "string",
        "description": "The math expression to evaluate"
      }
    },
    "required": ["input"]
  }
}
```

---

## Test

Ask:
```
What is 2 + 2?
```

✅ Expected Output:
```
4
```

---

## 🛠 Common Errors

### ❌ `I don’t know how to do that.`
- Cause: Agent doesn’t know it can use tools.

### ❌ `400 Invalid schema for function 'calculator': Missing 'input'`
- Cause: Calculator tool not using valid schema (missing `required: ["input"]`)

---
## 🧰 Final Working Setup after simplifying the Agentflow (removing the separate tool that was making the call complkicated)


## 📸 Screenshot Example

> Add screenshots here once hosted (optional).

---

## ✅ References
