from expLib import main as expenses
import  argparse

tracker = expenses.dtman()
parser = argparse.ArgumentParser()
parser.add_argument("--add", help="Add expense entry in the tracker", action="store_true")
parser.add_argument("--desc","--description", help="Help user Add description to their expense")
parser.add_argument("--amnt" , "--amount" , help="Help user add amount to their expenses")
args = parser.parse_args()
if args.add and args.desc == str and args.add_argument == int:
        tracker.add_entry(args.description, args.amount)
        print(f"Expense of {args.description} added succesfully of amount {args.amount}")
