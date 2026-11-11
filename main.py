from expLib import main as expenses
import  argparse

tracker = expenses.dtman()
parser = argparse.ArgumentParser()
parser.add_argument("--add", help="Add expense entry in the tracker", action="store_true")
parser.add_argument("--desc","--description", dest="description" ,help="Help user Add description to their expense")
parser.add_argument("--amnt" , "--amount" , type=int , help="Help user add amount to their expenses")
args = parser.parse_args()
if args.add==True and args.description == str and args.amount == int:
   print(f"New expense entry for {args.description} for {args.amount}")