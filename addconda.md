## Step 1: Create a Conda environment.
```
conda create --name ml python=3.9y
# 選 y 進行安裝
conda activate ml
conda install pandas matplotlib seaborn scikit-learn
conda install jupyter notebook ipykernel
# or
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=ml
```
