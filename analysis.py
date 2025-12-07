# 23f3001448@ds.study.iitm.ac.in
# Marimo Notebook: Interactive Data Analysis
# This notebook shows variable dependencies, interactivity, and documentation.

import marimo as mo

# Create the Marimo app
app = mo.App()

# -----------------------------
# Cell 1: Base data definition
# -----------------------------
# This cell defines the base dataset.
# Other cells DEPEND on `data`.
@app.cell
def __():
    # Example dataset: could be anything numerical
    data = [10, 20, 30, 40, 50]
    return data


# ------------------------------------
# Cell 2: Interactive slider widget
# ------------------------------------
# This cell defines a slider that controls the scaling factor.
# Other cells DEPEND on `slider`.
@app.cell
def __():
    slider = mo.ui.slider(start=1, end=10, value=5, label="Scale factor")
    return slider


# ------------------------------------------------
# Cell 3: Derived data (depends on data + slider)
# ------------------------------------------------
# This cell shows variable dependency:
#   - It uses `data` from Cell 1
#   - It uses `slider` from Cell 2
@app.cell
def __(data, slider):
    scaled_data = [x * slider.value for x in data]
    return scaled_data


# -------------------------------------------------
# Cell 4: Dynamic markdown (depends on slider + data)
# -------------------------------------------------
# This cell produces Markdown output based on the state of `slider`
# and the computed `scaled_data`. It is reactive.
@app.cell
def __(slider, scaled_data):
    md = mo.md(
        f"""
### 📊 Interactive Data Scaling Demo

- Slider value: **{slider.value}**
- Original data: `{[10, 20, 30, 40, 50]}`
- Scaled data: **{scaled_data}**

Move the slider to instantly update the scaled data.
"""
    )
    return md


# Run the app when executed as a script
if __name__ == "__main__":
    app.run()
