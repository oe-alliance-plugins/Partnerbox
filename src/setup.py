from setuptools import setup
import setup_translate

pkg = 'Extensions.Partnerbox'
setup(name='enigma2-plugin-extensions-partnerbox',
       version='3.0',
       description='Partnerbox (Remote Bouquets, Channels, Timers and TV Player)',
       package_dir={pkg: 'Partnerbox'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
