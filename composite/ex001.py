from abc import ABC, abstractmethod
import pathlib
from typing import List, Optional

"""
Applicability
 Use the Composite pattern when you have to implement a tree-like
 object structure.

 The Composite pattern provides you with two basic element types that
 share a common interface: simple leaves and complex containers. A container
 can be composed of both leaves and other containers. This lets
 you construct a nested recursive object structure that resembles a tree.

 Use the pattern when you want the client code to treat both simple and
 complex elements uniformly.

 All elements defined by the Composite pattern share a common interface.
 Using this interface, the client doesn't have to worry about the concrete
 class of the objects it works with.

 How to Implement
Make sure that the core model of your app can be represented as a
tree structure. Try to break it down into simple elements and containers.
Remember that containers must be able to contain both simple elements and
other containers.

Declare the component interface with a list of methods that make sense
for both simple and complex components.

Create a leaf class to represent simple elements. A program may have
multiple different leaf classes.

Create a container class to represent complex elements. In this class,
provide an array field for storing references to sub-elements. The array
must be able to store both leaves and containers, so make sure it's
declared with the component interface type.

While implementing the methods of the component interface, remember
that a container is supposed to be delegating most of the work to sub-elements.

Finally, define the methods for adding and removal of child elements
in the container.

Keep in mind that these operations can be declared in the component
interface. This would violate the Interface Segregation Principle because
the methods will be empty in the leaf class. However, the client will be
able to treat all the elements equally, even when composing the tree.

Pros and Cons
 Pros:
  You can work with complex tree structures more conveniently: use
  polymorphism and recursion to your advantage.
  Open/Closed Principle. You can introduce new element types into the app
  without breaking the existing code, which now works with the object tree.

 Cons
  It might be difficult to provide a common interface for classes whose
  functionality differs too much. In certain scenarios, you'd need to
  overgeneralize the component interface, making it harder to comprehend.

Relations with Other Patterns
You can use Builder when creating complex Composite trees because you
can program its construction steps to work recursively.

Chain of Responsibility is often used in conjunction with Composite.
In this case, when a leaf component gets a request, it may pass it
through the chain of all of the parent components down to the root of
the object tree.

You can use Iterators to traverse Composite trees.

You can use Visitor to execute an operation over an entire Composite tree.

You can implement shared leaf nodes of the Composite tree as Flyweights
to save some RAM.

Composite and Decorator have similar structure diagrams since both rely
on recursive composition to organize an open-ended number of objects.

A Decorator is like a Composite but only has one child component.
There's another significant difference: Decorator adds additional
responsibilities to the wrapped object, while Composite just “sums up”
its children's results.

However, the patterns can also cooperate: you can use Decorator
to extend the behavior of a specific object in the Composite tree.

Designs that make heavy use of Composite and Decorator can often
benefit from using Prototype. Applying the pattern lets you clone
complex structures instead of re-constructing them from scratch.
"""


class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

    @abstractmethod
    def create(self, base_path: pathlib.Path):
        pass


class File(FileSystemComponent):
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

    def show_details(self):
        print(f"File: {self.name}")

    def create(self, base_path: pathlib.Path):
        file_path = base_path / self.name
        file_path.touch()
        file_path.write_text(self.content)


class Directory(FileSystemComponent):
    def __init__(
        self,
        name,
        components: Optional[List[FileSystemComponent]] = None
    ) -> None:
        self.name = name
        self.components: List[FileSystemComponent] = []

        if components:
            self.components = components

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def show_details(self):
        print(f"Directory: {self.name}")
        for component in self.components:
            component.show_details()

    def create(self, base_path: pathlib.Path):
        dir_path = base_path / self.name
        if not dir_path.exists():
            dir_path.mkdir()
        for component in self.components:
            component.create(dir_path)


def create_file_structure(
    component: FileSystemComponent,
    base_path_str: str
):
    base_path = pathlib.Path(base_path_str)
    if not base_path.exists():
        base_path.mkdir(parents=True)

    component.create(base_path)


if __name__ == "__main__":

    file1 = File("file1.txt", "File1 content!")
    file2 = File("file2.txt", "File2 content!")
    file3 = File("file3.txt", "File3 content!")
    file4 = File("file4.txt", "File4 content!")
    file5 = File("file5.txt", "File5 content!")

    sub_sub_dir2 = Directory("subsubdir2")
    sub_dir2 = Directory("subdir2", [file5, sub_sub_dir2])
    sub_sub_dir1 = Directory("subsubdir1", [file3, file4])
    sub_dir1 = Directory("subdir1", [sub_sub_dir1, file2])

    root_dir = Directory("root", [file1, sub_dir1, sub_dir2])

    root_dir.show_details()

    create_file_structure(root_dir, ".")
