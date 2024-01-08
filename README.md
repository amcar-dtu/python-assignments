# python-assignments

To print the Jupyter Notebook you can use [`nbconvert`](https://github.com/jupyter/nbconvert):

```bash
$ jupyter nbconvert --to <output format> <input notebook>
```

## Example: export to PDF

Convert Jupyter notebook file, `mynotebook.ipynb`, to PDF using:

```bash
$ jupyter nbconvert mynotebook.ipynb --to pdf --no-input
```
