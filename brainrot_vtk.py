#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2

from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOImage import vtkPNGReader
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkImageActor
)
def main():
    colors = vtkNamedColors()

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('xiii')
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    rgb = [3,255,18]
    lin_color = []

    for color in rgb:
        color_rgb = color/255
        lin_color.append(color_rgb)
    
    renderer.SetBackground(lin_color[0],lin_color[1],lin_color[2])

    png_reader = vtkPNGReader()
    png_reader.SetFileName("D:\\brainrot.png")
    png_reader.Update()

    image_actor = vtkImageActor()
    image_actor.GetMapper().SetInputConnection(png_reader.GetOutputPort())

    image_actor.SetPosition(0, 0, 0)

    renderer.AddActor(image_actor)
    renderer.GetActiveCamera().Azimuth(00)
    renderer.GetActiveCamera().Elevation(00)
    renderer.ResetCamera()
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
