# Custom Structural Field Validators with Pydantic

A Python processing script illustrating how to build custom element mutators and restrictive email domain constraints using **Pydantic V2**.

## 🚀 Features

- **String Transformation Validator**: Automatically mutates input names to safe uppercase strings (`value.upper()`) at the schema validation level.
- **Strict Domain Whitelisting**: Intercepts email addresses to strictly permit corporate domains (`hbl.com`, `ubl.com`), raising clear errors for any alternative handlers.
- **Built-in Email Validation**: Uses Pydantic's specialized `EmailStr` field type to natively check for standard syntactical email formats before custom logic triggers.

## 📦 Installation Prerequisites

Ensure you have Python installed, then install Pydantic with the optional standard email validation dependencies:

```bash
pip install "pydantic[email]"
```

## 💻 Script Implementation (`main.py`)

```python
from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    allergies: List[str]
    phone: Dict[str, str]

    @field_validator('name')
    @classmethod
    def name_validator(cls, value: str) -> str:
        # Enforces capitalization across model instance mutations
        return value.upper()

    @field_validator('email')
    @classmethod
    def email_validator(cls, value: str) -> str:
        # Strict whitelisting filter logic
        valid_domains = ["hbl.com", "ubl.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError(f"Invalid domain name. Please choose from {valid_domains}")
        return value

def show_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.phone)

# Scenario Valid Configuration Payload
patient_info = {
    "name": "john doe",  # Inputted lowercase, will mutate to uppercase
    "email": "john.doe@hbl.com",
    "age": 30,
    "weight": 70.5,
    "allergies": ["pollen", "dust"],
    "phone": {"home": "123-456-7890", "work": "987-654-3210"}
}

patient1 = Patient(**patient_info)
show_patient(patient1)
```

## 🎯 Validation Verification Output

Executing this script via your console terminal tool layout:

```bash
python main.py
```

Output:
```text
JOHN DOE
john.doe@hbl.com
30
70.5
['pollen', 'dust']
{'home': '123-456-7890', 'work': '987-654-3210'}
```

---

## 🧪 Constraint Error Scenarios

When un-vetted input blocks fail our runtime constraint handlers, Pydantic cleanly drops processing execution with the following message structures:

### 1. Domain Boundary Mismatch Violation (`email: "user@gmail.com"`)
```text
1 validation error for Patient
email
  Value error, Invalid domain name. Please choose from ['hbl.com', 'ubl.com'] [type=value_error, input_value='user@gmail.com', input_type=str]
```

### 2. Invalid Email Format Rejection (`email: "not-an-email"`)
```text
1 validation error for Patient
email
  An email address must have an @ sign. [type=value_error, input_value='not-an-email', input_type=str]
```
