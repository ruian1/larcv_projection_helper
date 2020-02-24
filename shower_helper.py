import ROOT
import utility as u

def larlite_shower_to_contour(whole_image, larlite_shower, plane = 2):

    x, y, z = larlite_shower.ShowerStart().x(), larlite_shower.ShowerStart().y(), larlite_shower.ShowerStart().z()
    shower_start_x_2d = ROOT.Double()
    shower_start_y_2d = ROOT.Double()
    # 
    shower_start_x_2d, shower_start_y_2d =u.Project3Dto2D_and_fliplr(whole_image.meta(),
                                                                     x,
                                                                     y,
                                                                     z, plane,
                                                                     shower_start_x_2d,
                                                                     shower_start_y_2d)

    x_dir, y_dir, z_dir = larlite_shower.Direction().x(), larlite_shower.Direction().y(), larlite_shower.Direction().z()
    shower_length = larlite_shower.Length()
    print "shower_length, ", shower_length
    shower_width = larlite_shower.Width()

    shower_end_x = x + x_dir * shower_length
    shower_end_y = y + y_dir * shower_length
    shower_end_z = z + z_dir * shower_length

    shower_end_x_2d = ROOT.Double()
    shower_end_y_2d = ROOT.Double()
    shower_end_x_2d, shower_end_y_2d =u.Project3Dto2D_and_fliplr(whole_image.meta(),
                                                                 shower_end_x,
                                                                 shower_end_y,
                                                                 shower_end_z, plane,
                                                                 shower_end_x_2d,
                                                                 shower_end_y_2d)

    return shower_end_x_2d, shower_end_y_2d
