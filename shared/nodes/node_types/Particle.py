from ..Node import Node

# Particle
class Particle(Node):
    class_name = "Particle"
    fields = []

    # Make approximation HSD struct from blender data.
    @classmethod
    def fromBlender(cls, blender_obj):
        pass

    # Make approximation Blender object from HSD data.
    def toBlender(self, context):
        pass