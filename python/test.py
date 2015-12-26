import os

from utils import  open_osx

from convolutions import convolve_signals
from signals import Signal

# add to python path
ESPACES_PROJECT = os.environ['ESPACES_PROJECT']

if __name__:

    # impulse reponse 
    path_ir = os.path.join(ESPACES_PROJECT,'data','examples','ir.wav')
    sig_ir = Signal(path_ir,mono=True)

    # audio example
    path_ex = os.path.join(ESPACES_PROJECT,'data','examples','speech.wav')
    sig_ex = Signal(path_ex,mono=True)

    # convolved signal
    mode = 'full' # 'full' or 'valid' or 'same'
    kind = 'ola' # 'ola' or 'ss'

    sig_cv = convolve_signals(sig_ex, sig_ir, mode, kind)

    # save audio and image
    for name in ['ex','ir','cv']:
        save_path = os.path.join(ESPACES_PROJECT,'data','examples','to_erase_'+name+'_'+kind)
        save_au = save_path+'_'+mode+'.wav'
        save_im = save_path+'_'+mode+'.png'
        sig = locals()['sig_'+name]
        sig.write(save_au)
        sig.save_image(save_im, title=name+' '+mode+' '+kind)
        open_osx(save_au,save_im)