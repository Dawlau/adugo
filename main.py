from App import App
import time

if __name__ == "__main__":
	app = App()

	start = time.time()
	app.run()
	end = time.time()

	print("Jocul a rulat: ", end - start)