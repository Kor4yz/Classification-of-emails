import typer, pathlib
from .train import train_models
from .evaluate import evaluate_models
from .data import load_raw
from .preprocess import make_dataset

app = typer.Typer(help="Email Classification CLI")

@app.command()
def prepare(input_csv: str, out_dir: str="data/processed"):
    df = load_raw(input_csv)
    X_train, X_test, y_train, y_test = make_dataset(df, out_dir)
    typer.echo(f"Saved to {out_dir}")

@app.command()
def train(cfg: str=""):
    train_models(cfg)

@app.command()
def evaluate(out_dir: str="artifacts"):
    metrics = evaluate_models(out_dir)
    typer.echo(metrics)

if __name__ == "__main__":
    app()
