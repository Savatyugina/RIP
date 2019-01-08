import rectangle
import circle
import foursquare

def main():
        rec = rectangle.Rectangle(3,2,"синий")
        cir = circle.Circle(5,"зеленый")
        four = foursquare.Quadrate(5, "красный")

        print(rec)
        print(cir)
        print(four)


if __name__ == "__main__":
    main()