# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApeglm(RPackage):
    """apeglm provides Bayesian shrinkage estimators for effect sizes for a variety of GLM models, using approximation of the posterior for individual coefficients."""

    bioc = "apeglm"

    version("1.22.1", sha256="477372ab998a0ef36da5992f140ec3bd08fb7a9a2430840235be0f3b2fac21a7")

    depends_on("r-biocinstaller", type=("build", "run"))

