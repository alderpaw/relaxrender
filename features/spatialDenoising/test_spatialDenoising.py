

import unittest

from features.spatialDenoising.clear_noise import ClearNoise


class TestSpatialDenoising(unittest.TestCase):

    def test_spatialDenoising(self):

        clear = ClearNoise()

        images = clear.clear_noise()

        if len(images)<=1:
            pix1 = images[0]
            pix2 = images[1]

            w, h = images[0].size
            w -= 1
            h -= 1

            tot = 0

            for i in range(0, w):
                for j in range(0, h):
                    tmp = abs(pix1[j, i] - pix2[j, i])
                    tot += tmp / 255

            t = tot / (w * h)

            self.assertTrue(t <= 0.1)



if __name__ == '__main__':
    unittest.main()
