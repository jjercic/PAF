xs = np.linspace(-5, 5, 20)
    ys = k * xs + l

    plt.title("Pravac")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.plot(xs, ys)
    plt.plot(xa, ya, marker="o")
    plt.plot(xb, yb, marker="o")
    
    opt = input("Spremi graf (S) ili Prikaži graf (P): ")
    if opt == "P":
        plt.show()