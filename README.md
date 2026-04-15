# Tiered Phone Plan Calculator

##  Overview

In this assignment, you will build a Python program that calculates a monthly phone bill based on data usage.

This assignment builds on your previous work with input, variables, and calculations by adding more advanced decision-making.

The goal is to practice:
- Using `if-elif-else` statements to handle multiple cases
- Writing nested decision statements
- Using logical operators (`and`, `or`, `not`)
- Creating and using boolean variables
- Combining calculations with decision logic


###  What You Are Building

You will write a program that:
- Calculates how much data a user has gone over their plan limit
- Applies different pricing rules depending on usage
- Adjusts pricing based on whether the user has a premium plan
- Displays the final bill and helpful messages

---



## Program Inputs

Ask the user to enter:
- Data used (in GB)
- Base monthly plan cost
- Whether they have a premium plan (`yes` or `no`)

---

### Pricing Rules

- The plan includes **10 GB** of data.

- If the user uses **10 GB or less**:
  - No overage charges are applied

- If the user uses **more than 10 GB but no more than 20 GB**:
  - Regular users pay **$2 per GB** over the limit
  - Premium users pay **$1 per GB** over the limit

- If the user uses **more than 20 GB**:
  - Regular users pay **$3 per GB** over the limit
  - Premium users pay **$2 per GB** over the limit

- Your overage cost is equal to your overage gb multiplied by your overage rate
- Your total bill is equal to your base cost plus your overage cost

---

### Program Requirements

Your program must:

#### Use `if-elif-else`
You must use an `if-elif-else` structure to handle the three data usage tiers.

#### Use a nested decision
Inside at least one of your cases, use a nested decision structure to determine the correct overage rate.

#### Use a boolean variable
Store whether the user has a premium plan in a boolean variable (for example, `has_premium`).

#### Use a logical operator
Use at least one logical operator (`and`, `or`, or `not`) in a condition.

#### Use variables in your decision structure to reference later
Use varaibles to track overage cost across the different scenerios. Use them when calculating your total bill after your program has finished evaluating your decisions. 

#### Perform calculations
Your program must calculate:
- How many GB over the limit the user is
- The overage cost
- The total bill

---

### Output

#### Requirements

Your program must display:
- The number of GB over the limit
- The overage cost
- The total monthly bill


#### Sample Runs

```
Enter data used (GB): 8
Enter base monthly plan cost: 40
Do you have a premium plan? (yes or no): no

You are within your data limit.
GB over limit: 0
Overage cost: $0.00
Total bill: $40.00
```

```
Enter data used (GB): 25
Enter base monthly plan cost: 40
Do you have a premium plan? (yes or no): no

You are 15.0 GB over your limit.
Overage rate: $3 per GB
Overage cost: $45.00
Total bill: $85.00
```

---

## Files

You will work with the following files:
- `data_bill.py` — your Python program

Do not create additional program files.

---

## Submission

Submit a link to your automatically generated Feedback PR to the Canvas assignment. 