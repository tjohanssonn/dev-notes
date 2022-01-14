# Interfaces

Interfaces doesn't really exist in C++ since there is no keyword for it as in e.g. C# or Java. A similar functionality can be created though using _pure virtual functions_.

```cpp
// An interface class using pure virtual functions (= 0, i.e. no body)
class shape
{
  public:
    virtual ~shape() {};
    virtual void move_x(int x) = 0;
    virtual void move_y(int y) = 0;
    virtual void draw() = 0;
//...
};

// Class implementing the interface declared in 'shape' class.
class line : public shape
{
  public:
    virtual ~line();
    virtual void move_x(int x); // implements move_x
    virtual void move_y(int y); // implements move_y
    virtual void draw(); // implements draw
  private:
    point end_point_1, end_point_2;
//...
};
```

From [Wikipedia](https://en.wikibooks.org/wiki/More_C%2B%2B_Idioms/Interface_Class):

> "Every interface class should have a virtual destructor. Virtual destructor makes sure that when a shape is deleted polymorphically, correct destructor of the derived class is invoked."
