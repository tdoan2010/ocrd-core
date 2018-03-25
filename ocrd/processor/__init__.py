class Processor(object):
    """
    A processor runs an algorithm based on the workspace, the mets.xml in the
    workspace (and the input files defined therein) as well as optional
    parameters.
    """

    def __init__(self, workspace, parameters=None, inputGrp="INPUT", outputGrp="OUTPUT"):
        self.workspace = workspace
        self.inputGrp = inputGrp
        self.outputGrp = outputGrp
        self.parameters = parameters if parameters is not None else {}

    def verify(self):
        """
        Verify that the input is fulfills the processor's requirements.
        """
        return True

    def process(self):
        """
        Process the workspace
        """
        raise Exception("Must be implemented")

    @property
    def input_files(self):
        """
        List the input files
        """
        return self.workspace.mets.files_in_group(self.inputGrp)

    def add_output_file(self, input_file=None, basename=None, **kwargs):
        """
        Add an output file.
        """
        if basename is None and input_file is not None:
            basename = input_file.basename_without_extension + '.xml'
        self.workspace.add_file(self.outputGrp, basename=basename, **kwargs)